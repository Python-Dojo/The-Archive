#include <type_traits>
//template<intergral StoreageType>
using StoreageType = unsigned long long;

template<typename T>
concept AnyInt = std::is_integral<T>::value;
template<typename T>
concept AnyFloat = std::is_floating_point<T>::value;
template<typename T>
concept Number = (AnyFloat<T> || AnyInt<T>);

class Fraction;

constexpr Fraction ConvertFloatToFraction(const AnyFloat auto toConvert);

class Fraction
{
public:
    template<AnyInt IntLike = unsigned int>
    constexpr Fraction(const IntLike nominator, const IntLike denominator = 1U)
        : m_nominator(nominator), m_denominator(denominator) {};

    constexpr Fraction(const AnyFloat auto converatble)
    {
        // feels hacky but think it's fine
        *this = ConvertFloatToFraction(converatble);
    };

    template<AnyFloat PrecisionType = long double>
    constexpr PrecisionType GetDecimal() const noexcept
    {
        return static_cast<PrecisionType>(m_nominator) / m_denominator;
    }

    constexpr auto operator <=>(const Fraction& other)
    {
        return this->GetDecimal() <=> other.GetDecimal();
    }

    constexpr Fraction operator+(const Fraction& other)
    {
        return Fraction( 
        (m_nominator * other.m_denominator) + (other.m_nominator * m_denominator),
            m_denominator * other.m_denominator);
    }

    constexpr Fraction operator+(const Number auto intLike)
    {
        return *this + Fraction(intLike);
    }

    constexpr Fraction operator-(const Fraction& other)
    {
        return Fraction(
        (m_nominator * other.m_denominator) - (other.m_nominator * m_denominator),
            m_denominator * other.m_denominator );
    }

    constexpr Fraction operator-(const Number auto intLike)
    {
        return *this - Fraction(intLike);
    }

    constexpr Fraction operator/(const Fraction& other)
    {
        return Fraction(m_nominator * other.m_denominator,
            m_denominator * other.m_nominator );
    }

    constexpr Fraction operator/(const Number auto intLike)
    {
        return *this + Fraction(intLike);
    }

    constexpr Fraction operator* (const Fraction& other)
    {
        return Fraction( m_nominator * other.m_nominator , 
            m_denominator * other.m_denominator );
    }

    constexpr Fraction operator* (const Number auto anyNumber)
    {
        return *this + Fraction(anyNumber);
    }

private:
    StoreageType m_nominator{ 0 };
    StoreageType m_denominator{ 1 };
};

unsigned long long inline RoundToInt(const long double& toRound)
{
    return static_cast<unsigned long long>(std::round(toRound));
}

constexpr Fraction HighPrecisionFloatToFraction(
    const long double& toConvert, const long double largestPossibleMultiplier)
{
    return Fraction(
        RoundToInt(toConvert * largestPossibleMultiplier),
        RoundToInt(largestPossibleMultiplier)
    );
}

// a double with high precision (multiplied by 0.9 to get higher precision)
constexpr auto longDoubleMax = std::numeric_limits<long double>::max() * 0.9;

constexpr Fraction ConvertFloatToFraction(const AnyFloat auto toConvert)
{
    const auto highPrecisionToConvert = static_cast<long double>(toConvert);

    // so if 2 > toConvert > 1 then use doubleMax/2 as denominator
    const auto denominator = longDoubleMax / std::ceil(highPrecisionToConvert);

    return HighPrecisionFloatToFraction(highPrecisionToConvert, denominator);
}

constexpr Fraction operator""_F(const long double decimal)
{
    return ConvertFloatToFraction(decimal);
}

constexpr Fraction StringToFraction(const std::string& toConvert)
{
    if (std::string::npos != toConvert.find("."))
    {
        return ConvertFloatToFraction(std::stold(toConvert));
    }

    auto fracPoint = toConvert.find("/");

    if (std::string::npos == fracPoint) 
    {
        fracPoint = toConvert.find("\\");
    }

    // No slashes or decimal points so must be an int?
    if (std::string::npos == fracPoint)
    {
        return Fraction(std::stoll(toConvert));
    }

    const auto numiartor = std::stoll(toConvert.substr(0U, fracPoint));
    const auto denominator = std::stoll(toConvert.substr(fracPoint + 1 ));

    //if (0 != denominator)
    {
        return Fraction(numiartor, denominator);
    }
}

constexpr Fraction operator""_F(const char* asString)
{
    return StringToFraction(asString);
}

constexpr Fraction operator""_F(const char* str, size_t size)
{
    return StringToFraction(str);
}

// Try to avoid C++ helping by calculating stuff at compile time
// Again this is to AVOID optimisation.
float GetAFloat(std::string& double_);

#define PrintFractionTest(Test, ExpectedResult) std::cout << "\n" #Test " was " << (Test).GetDecimal() << " should be: " #ExpectedResult

#define PrintRegularTest(Test, Expected) std::cout << "\n" #Test " was " << (Test) << " should be " #Expected

int main()
{
    std::cout << std::setprecision(9);
    PrintFractionTest(Fraction(2, 10) + Fraction(4, 2), 2.2);
    PrintFractionTest(0.2_F + 2_F, 2.2);
    PrintFractionTest(1_F / 2 + 1, 1.5);
    PrintFractionTest("1/2"_F + 1, 1.5);
    PrintFractionTest(StringToFraction("1234/5678") + StringToFraction("3.1415"), 3.588300);
    PrintFractionTest(Fraction(1) + Fraction(4), 5);
    PrintFractionTest(Fraction(5, 2) * Fraction(6, 1) - Fraction(6, 3), 13);
    PrintFractionTest(Fraction(1, 10) + Fraction(2, 10), 0.3);
    // 0.1 + 0.2 will be compiled out so do this stuff
    using namespace std::string_literals;
    auto one = "0.1"s;
    auto two = "0.2"s;
    PrintRegularTest(GetAFloat(one) + GetAFloat(two), 0.3);
}

// To avoid inline optimisation (forward declared previously
float GetAFloat(std::string& value)
{
    const auto copy = std::stold(value);
    return copy;
}
