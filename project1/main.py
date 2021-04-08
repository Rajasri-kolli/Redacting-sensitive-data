import redactor
import argparse

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  help="Input Files", nargs='*', action='append')
    parser.add_argument("--names", help="Redact_names", action='store_true')
    parser.add_argument("--gender", help="Redact_genders", action='store_true')
    parser.add_argument("--dates",  help="Redact_dates", action='store_true')
    parser.add_argument("--stats",  help="Redact_stats", action='store_true')
    parser.add_argument("--concept", help="Redact concept words")
    parser.add_argument("--output", help="Output Files")

    args = parser.parse_args()

    x = redactor.read_input(args.input)

    if (args.names):
         x = redactor.get_names(x)
    if (args.gender):
         x = redactor.get_gender(x)
    if (args.dates):
         x = redactor.get_dates(x)
    if (args.concept):
         x = redactor.get_concept(x, args.concept)
    if (args.output):
        redactor.Output(args.input, x, args.output)
    if (args.stats):
        redactor.get_stats()

