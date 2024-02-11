import os.path
from math import ceil
from services.sheet_utils import update_cell, update_naf, print_student_info

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1uYa4Eo6Os3fdbF1YK8fvIxlcyzvBxIpPjpMIJwdOhZ8"
RANGE_NAME = "engenharia_de_software!A4:F27"


def main():
    creds = None

    if os.path.exists("config/token.json"):
        creds = Credentials.from_authorized_user_file("config/token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "config/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("config/token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
            .execute()
        )

        grades = result['values']

        for index, grade_row in enumerate(grades, start=4):
            total_score = 0
            naf = 0

            for score in grade_row[3:]:
                total_score += int(score)
            average_score = total_score / 3

            max_absences = 15
            if int(grade_row[2]) > max_absences:
                update_cell(sheet, SPREADSHEET_ID, f"G{index}", "Reprovado por falta")
                print_student_info(grade_row[1], grade_row[0], average_score, "Reprovado por falta",
                                   num_absences=int(grade_row[2]))
            elif average_score < 50:
                update_cell(sheet, SPREADSHEET_ID, f"G{index}", "Reprovado por nota")
                print_student_info(grade_row[1], grade_row[0], average_score, "Reprovado por nota")
            elif 70 > average_score >= 50:
                update_cell(sheet, SPREADSHEET_ID, f"G{index}", "Exame final")
                naf = ceil(100 - average_score)
                print_student_info(grade_row[1], grade_row[0], average_score, "Exame final", naf)
            else:
                update_cell(sheet, SPREADSHEET_ID, f"G{index}", "Aprovado")
                print_student_info(grade_row[1], grade_row[0], average_score, "Aprovado")

            update_naf(sheet, SPREADSHEET_ID, f"H{index}", naf)

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
