from datetime import timedelta
from email_sender import send_mail
from report_formatter import plain_text_format, line_chart_format
from report_generator import generate_report


class CpuReporter:
    def __init__(self, generator, formatter, sender):
        self.__generator = generator
        self.__formatter = formatter
        self.__sender = sender

    def send_report(self):
        report = self.__generator(duration=timedelta(seconds=3))
        formatted = self.__formatter(report)
        self.__sender(formatted)


def execution():
    plain_text_reporter = CpuReporter(
        generator=generate_report,
        formatter=plain_text_format,
        sender=send_mail
    )

    fancy_reporter = CpuReporter(
        generator=generate_report,
        formatter=line_chart_format,
        sender=send_mail
    )

    fancy_reporter.send_report()


if __name__ == '__main__':
    execution()