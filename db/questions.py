from db.database import get_db
from db.queries import GET_ALL_QUESTIONS, GET_QUESTION_BY_ID, INSERT_QUESTION


def get_all_questions():
    conn = get_db()
    rows = conn.execute(GET_ALL_QUESTIONS).fetchall()
    print(rows)
    conn.close()
    return [dict(r) for r in rows]


def get_question(question_id: int):
    conn = get_db()
    row = conn.execute(GET_QUESTION_BY_ID, (question_id, )).fetchone()
    conn.close()
    return dict(row) if row else None


def add_question(question_text: str, correct_answer: str):
    conn = get_db()
    conn.execute(INSERT_QUESTION, (question_text, correct_answer))
    conn.commit()
    conn.close()