# student_psych_profile 表 DAO 数据访问层
from sqlalchemy.orm import Session
from model.student_models import StudentPsychProfile


def psych_profile_upsert(db: Session, profile) -> StudentPsychProfile:
    """创建或更新心理画像记录（按student_id唯一键upsert）"""
    db_profile = db.query(StudentPsychProfile).filter(
        StudentPsychProfile.student_id == profile.student_id
    ).first()

    if db_profile:
        if profile.latest_emotion_tag is not None:
            db_profile.latest_emotion_tag = profile.latest_emotion_tag
        if profile.emotion_score is not None:
            db_profile.emotion_score = profile.emotion_score
        if profile.last_interaction_time is not None:
            db_profile.last_interaction_time = profile.last_interaction_time
        if profile.emotion_history is not None:
            db_profile.emotion_history = profile.emotion_history
    else:
        db_profile = StudentPsychProfile(
            student_id=profile.student_id,
            latest_emotion_tag=profile.latest_emotion_tag,
            emotion_score=profile.emotion_score,
            last_interaction_time=profile.last_interaction_time,
            emotion_history=profile.emotion_history
        )
        db.add(db_profile)

    db.commit()
    db.refresh(db_profile)
    return db_profile
