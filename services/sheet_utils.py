def update_status(sheet, spreadsheet_id, cell_range, status):
    """
    Updates the status of a cell in a Google Sheets spreadsheet.

    Parameters:
    - sheet: The Google Sheets API service object.
    - spreadsheet_id: The ID of the spreadsheet to update.
    - cell_range: The range of cells to update in A1 notation (e.g., "Sheet1!A1:B2").
    - status: The new status value to be set in the cell.

    Returns: None
    """
    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=cell_range,
        valueInputOption="USER_ENTERED",
        body={'values': [[status]]}
    ).execute()


def update_naf(sheet, spreadsheet_id, cell_range, naf_score):
    """
    Updates the NAF (minimum passing score) of a cell in a Google Sheets spreadsheet.

    Parameters:
    - sheet: The Google Sheets API service object.
    - spreadsheet_id: The ID of the spreadsheet to update.
    - cell_range: The range of cells to update in A1 notation (e.g., "Sheet1!A1:B2").
    - naf_score: The new NAF (minimum passing score) value to be set in the cell.

    Returns: None
    """
    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=cell_range,
        valueInputOption="USER_ENTERED",
        body={'values': [[naf_score]]}
    ).execute()


def print_student_info(name, student_id, average_score, final_result, naf=0, num_absences=0):
    """
    Prints student information including name, ID, average score, final result, NAF (minimum passing score),
    and number of absences.

    Parameters:
    - name: The name of the student.
    - student_id: The ID of the student.
    - average_score: The average score of the student.
    - final_result: The final result of the student (e.g., "Passed", "Failed").
    - naf: The NAF (minimum passing score) of the student (default is 0).
    - num_absences: The number of absences of the student (default is 0).

    Returns: None
    """
    print(f"Aluno (a): {name} | Mat.: {student_id} | Média: {round(average_score, 2)} "
          f"| Situação: {final_result}")

    if num_absences > 0:
        print(f"Número de faltas: {num_absences}")

    if naf > 0:
        print(f"Nota mínima para aprovação: {naf}")

    print("\n")
