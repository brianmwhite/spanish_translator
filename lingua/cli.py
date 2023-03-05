import cloup
from cloup import option_group, option
from cloup.constraints import RequireExactly
from translation.translation import SpanishTranslation
from unitconversion.unitconversion import UnitConversion


@cloup.command()
@option_group(
    "translation options",
    option("--number", help="a numerical string to translate to spanish"),
    option("--temp", help="temperature to convert between °C and °F"),
    option("--distance", help="distance to convert between km and miles"),
    option("--length", help="length to convert between feet/inches and meters/cm"),
    option("--weight", help="weight to convert between kg and lbs"),
    option(
        "--date",
        help="The date string to convert (in format "
        f'{", ".join(SpanishTranslation.DATE_FORMATS)})',
    ),
    constraint=RequireExactly(1),
)
def run(**kwargs):
    if kwargs.get("number"):
        sp = SpanishTranslation()
        print(sp.translate_number(kwargs.get("number"))[0])
    elif kwargs.get("date"):
        sp = SpanishTranslation()
        print(sp.translate_date(kwargs.get("date")))
    elif kwargs.get("temp"):
        uc = UnitConversion()
        input_temp_string = kwargs.get("temp")
        input_temp = uc.string_to_float(input_temp_string)
        
        c = uc.fahrenheit_to_celsius(input_temp)
        f = uc.celsius_to_fahrenheit(input_temp)
        
        print(
            f"{input_temp_string}°F > {c:.g}°C\n"
            f"{input_temp_string}°C > {f:g}°F"
        )
    elif kwargs.get("distance"):
        uc = UnitConversion()
        input_string = kwargs.get("distance")
        number = uc.string_to_float(input_string)
        km = uc.miles_to_km(number)
        m = uc.km_to_miles(number)
        
        print(
            f"{input_string} miles > {km:g} km\n"
            f"{input_string} km > {m:g} miles"
        )
    elif kwargs.get("weight"):
        uc = UnitConversion()
        input_string = kwargs.get("weight")
        number = uc.string_to_float(input_string)
        kg = uc.lb_to_kg(number)
        lbs = uc.kg_to_lb(number)
        
        print(
            f"{input_string} lbs > {kg:g} kg\n"
            f"{input_string} kg > {lbs:g} lbs"
        )
    elif kwargs.get("length"):
        uc = UnitConversion()
        input_string = kwargs.get("length")
        number = uc.string_to_float(input_string)
        kg = uc.lb_to_kg(number)
        lbs = uc.kg_to_lb(number)
        
        print(
            f"{input_string} lbs > {kg:g} kg\n"
            f"{input_string} kg > {lbs:g} lbs"
        )


if __file__ == "__main__" or __name__ == "__main__":
    run()
