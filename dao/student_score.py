# 学生成绩表 DAO 数据访问层
# 实现数据库的增删改操作

from sqlalchemy.orm import Session
from model.student_score import StudentScore
from schemas.student_score import ScoreCreate, ScoreUpdate


def score_create(db: Session, score: ScoreCreate):
    """创建新的学生成绩记录"""
    db_score = StudentScore(
        student_id=score.student_id,
        course_name=score.course_name,
        score=score.score,
        semester=score.semester
    )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def score_update(db: Session, score: ScoreUpdate):
    """根据ID更新学生成绩记录"""
    db_score = db.query(StudentScore).filter(StudentScore.id == score.id).first()
    if db_score:
        if score.student_id is not None:
            db_score.student_id = score.student_id
        if score.course_name is not None:
            db_score.course_name = score.course_name
        if score.score is not None:
            db_score.score = score.score
        if score.semester is not None:
            db_score.semester = score.semester
        db.commit()
        db.refresh(db_score)
    return db_score


def score_delete(db: Session, score_id: int):
    """根据ID删除学生成绩记录"""
    db_score = db.query(StudentScore).filter(StudentScore.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score