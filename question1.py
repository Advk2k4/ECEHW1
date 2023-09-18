class TimeConverter:
    @staticmethod
    def convert_seconds_to_dhms(seconds):
        seconds = int(seconds)
        time_units = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
        result = ""

        for unit, unit_seconds in time_units:
            if seconds >= unit_seconds:
                count = seconds // unit_seconds
                seconds %= unit_seconds
                if count > 1:
                    unit += "s"
                if result:
                    result += ", "
                result += f"{count} {unit}"

        return result if result else "0 seconds"

if __name__ == '__main__':
    print(TimeConverter.convert_seconds_to_dhms(1000))
    print(TimeConverter.convert_seconds_to_dhms(100))
