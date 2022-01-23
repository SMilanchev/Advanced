from datetime import datetime
from typing import List, Tuple
import matplotlib.pyplot as plt
import io
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def plain_text_format(report: List[Tuple[datetime, int, int]]):
    result = '\n'.join([
        time.strftime('%H:%M:%S.%f') + " " + str(cpu) + " " + str(memory)
        for time, cpu, memory in report
    ])

    return result


def line_chart_format(report):
    time = [time for time, _, _ in report]

    cpu_measurement = [cpu for _, cpu, _ in report]
    memory_measurement = [memory for _, _, memory in report]

    f = plt.figure()
    line_chart_1 = plt.plot(time, cpu_measurement, color='Red')
    line_chart_2 = plt.plot(time, memory_measurement, color='Blue')

    plt.xlabel('Time', color="green")
    plt.ylabel('CPU and Memory  Percentage Load', color="green")
    plt.title('CPU and Memory Percentage Load')
    plt.legend(['CPU Load', 'Memory Load'], loc=3)
    binary = io.BytesIO()
    f.savefig(binary, bbox_inches='tight')

    email = MIMEMultipart()
    part = MIMEBase("application", "octet-stream")

    part.set_payload(binary.getvalue())
    encoders.encode_base64(part)
    email.attach(part)

    return email
