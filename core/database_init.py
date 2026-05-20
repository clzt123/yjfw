from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from core.database import Base, engine
from model.sys_user import SysUser
from model.student_models import StudentAdminService, StudentPsychProfile, StudentPsychAlert, StudentFeedbackTicket, StudyAbroadProgress
from model.models import CourseProject, EventLecture, EventRegistration
from model.student_score import StudentScore
from model.employee_daily_report import EmployeeDailyReport
from model.crm_lead import CrmLead
from datetime import datetime, date
import bcrypt


def create_tables():
    """
    创建所有数据库表
    
    首先删除所有已存在的表，然后创建新表
    """
    print("正在删除现有表...")
    Base.metadata.drop_all(bind=engine)
    print("正在创建新表...")
    Base.metadata.create_all(bind=engine)
    print("表创建完成！")


def insert_test_data():
    """
    插入测试数据到各个表中（每张表10条）
    """
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # 插入用户数据（10条）
        print("正在插入测试用户数据...")
        hashed_password = bcrypt.hashpw("123456".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        users = [
            SysUser(username="admin", password=hashed_password, real_name="管理员", user_type="EMPLOYEE", employee_role="管理员", department="系统管理部", contact_info="13800138000", status="正常"),
            SysUser(username="student001", password=hashed_password, real_name="张三", user_type="STUDENT", department="计算机学院", contact_info="13800138001", status="正常"),
            SysUser(username="student002", password=hashed_password, real_name="李四", user_type="STUDENT", department="商学院", contact_info="13800138002", status="正常"),
            SysUser(username="student003", password=hashed_password, real_name="王五", user_type="STUDENT", department="外语学院", contact_info="13800138003", status="正常"),
            SysUser(username="student004", password=hashed_password, real_name="赵六", user_type="STUDENT", department="工程学院", contact_info="13800138004", status="正常"),
            SysUser(username="student005", password=hashed_password, real_name="钱七", user_type="STUDENT", department="艺术学院", contact_info="13800138005", status="正常"),
            SysUser(username="employee001", password=hashed_password, real_name="孙八", user_type="EMPLOYEE", employee_role="咨询师", department="咨询部", contact_info="13800138006", status="正常"),
            SysUser(username="employee002", password=hashed_password, real_name="周九", user_type="EMPLOYEE", employee_role="文案老师", department="文案部", contact_info="13800138007", status="正常"),
            SysUser(username="employee003", password=hashed_password, real_name="吴十", user_type="EMPLOYEE", employee_role="课程顾问", department="市场部", contact_info="13800138008", status="正常"),
            SysUser(username="employee004", password=hashed_password, real_name="郑十一", user_type="EMPLOYEE", employee_role="项目经理", department="项目部", contact_info="13800138009", status="正常"),
        ]
        db.add_all(users)
        
        # 插入课程项目数据（10条）
        print("正在插入测试课程项目数据...")
        courses = [
            CourseProject(project_name="雅思强化班", category="语言培训", target_education="本科", duration="3个月", tuition_fee="15000", project_advantage="名师授课，小班教学", application_condition="英语基础良好", target_country="英国", target_major="商科", status="招生中"),
            CourseProject(project_name="托福冲刺班", category="语言培训", target_education="本科", duration="2个月", tuition_fee="12000", project_advantage="一对一辅导，个性化学习", application_condition="英语四级以上", target_country="美国", target_major="工程", status="招生中"),
            CourseProject(project_name="背景提升科研项目", category="背景提升", target_education="本科", duration="6个月", tuition_fee="30000", project_advantage="名校教授指导，发表论文", application_condition="GPA 3.0以上", target_country="美国", target_major="计算机", status="招生中"),
            CourseProject(project_name="GRE备考课程", category="语言培训", target_education="硕士", duration="4个月", tuition_fee="18000", project_advantage="模块化教学，真题演练", application_condition="英语六级以上", target_country="美国", target_major="理科", status="招生中"),
            CourseProject(project_name="GMAT精英班", category="语言培训", target_education="硕士", duration="3个月", tuition_fee="16000", project_advantage="小班授课，模拟考试", application_condition="英语六级以上", target_country="美国", target_major="商科", status="招生中"),
            CourseProject(project_name="海外夏校项目", category="背景提升", target_education="高中", duration="1个月", tuition_fee="45000", project_advantage="美国名校体验，学分转换", application_condition="英语成绩优异", target_country="美国", target_major="未定", status="招生中"),
            CourseProject(project_name="日语N2考级班", category="语言培训", target_education="本科", duration="6个月", tuition_fee="10000", project_advantage="外教口语，考级保障", application_condition="零基础", target_country="日本", target_major="文科", status="招生中"),
            CourseProject(project_name="作品集辅导", category="背景提升", target_education="本科", duration="4个月", tuition_fee="25000", project_advantage="专业导师指导，作品集优化", application_condition="艺术类学生", target_country="英国", target_major="艺术", status="招生中"),
            CourseProject(project_name="德语B1课程", category="语言培训", target_education="本科", duration="4个月", tuition_fee="13000", project_advantage="中德双语教学，文化体验", application_condition="零基础", target_country="德国", target_major="工程", status="招生中"),
            CourseProject(project_name="AP课程辅导", category="背景提升", target_education="高中", duration="3个月", tuition_fee="20000", project_advantage="AP考试专家，高分保障", application_condition="高中在读", target_country="美国", target_major="理科", status="招生中"),
        ]
        db.add_all(courses)
        
        # 插入活动讲座数据（10条）
        print("正在插入测试活动讲座数据...")
        events = [
            EventLecture(event_name="英国留学申请分享会", event_type="线下", start_time=datetime(2024, 12, 20, 14, 0, 0), location="北京市朝阳区建国路88号", max_participants=100, current_participants=45),
            EventLecture(event_name="美国TOP30名校申请策略", event_type="线上", start_time=datetime(2024, 12, 25, 20, 0, 0), location="腾讯会议：123-456-789", max_participants=200, current_participants=120),
            EventLecture(event_name="加拿大留学移民规划", event_type="线下", start_time=datetime(2024, 12, 28, 10, 0, 0), location="上海市浦东新区陆家嘴金融中心", max_participants=80, current_participants=60),
            EventLecture(event_name="日本留学全攻略", event_type="线上", start_time=datetime(2024, 12, 30, 19, 0, 0), location="Zoom会议：987-654-321", max_participants=150, current_participants=85),
            EventLecture(event_name="澳洲八大名校解析", event_type="线下", start_time=datetime(2025, 1, 5, 14, 0, 0), location="广州市天河区珠江新城", max_participants=120, current_participants=78),
            EventLecture(event_name="欧洲留学费用解析", event_type="线上", start_time=datetime(2025, 1, 8, 20, 0, 0), location="腾讯会议：456-789-012", max_participants=180, current_participants=105),
            EventLecture(event_name="香港名校申请经验分享", event_type="线下", start_time=datetime(2025, 1, 12, 10, 0, 0), location="深圳市南山区科技园", max_participants=90, current_participants=55),
            EventLecture(event_name="新加坡留学优势分析", event_type="线上", start_time=datetime(2025, 1, 15, 19, 0, 0), location="钉钉会议：789-012-345", max_participants=160, current_participants=92),
            EventLecture(event_name="德国留学APS审核指导", event_type="线下", start_time=datetime(2025, 1, 18, 14, 0, 0), location="成都市锦江区春熙路", max_participants=60, current_participants=40),
            EventLecture(event_name="法国高商申请秘诀", event_type="线上", start_time=datetime(2025, 1, 22, 20, 0, 0), location="腾讯会议：234-567-890", max_participants=140, current_participants=70),
        ]
        db.add_all(events)
        
        # 插入活动报名数据（10条）
        registrations = [
            EventRegistration(event_id=1, customer_name="王五", phone="13800138003", email="wangwu@example.com", remark="想了解英国硕士申请", status="已报名"),
            EventRegistration(event_id=1, customer_name="赵六", phone="13800138004", email="zhaoliu@example.com", remark="本科申请咨询", status="已报名"),
            EventRegistration(event_id=2, customer_name="钱七", phone="13800138005", email="qianqi@example.com", remark="美国TOP50申请", status="已报名"),
            EventRegistration(event_id=3, customer_name="孙八", phone="13800138006", email="sunba@example.com", remark="移民倾向", status="已报名"),
            EventRegistration(event_id=4, customer_name="周九", phone="13800138007", email="zhoujiu@example.com", remark="日语学习中", status="已报名"),
            EventRegistration(event_id=5, customer_name="吴十", phone="13800138008", email="wushi@example.com", remark="澳洲本科", status="已报名"),
            EventRegistration(event_id=6, customer_name="郑十一", phone="13800138009", email="zheng11@example.com", remark="预算有限", status="已报名"),
            EventRegistration(event_id=7, customer_name="王十二", phone="13800138010", email="wang12@example.com", remark="香港授课型硕士", status="已报名"),
            EventRegistration(event_id=8, customer_name="李十三", phone="13800138011", email="li13@example.com", remark="新加坡国立", status="已报名"),
            EventRegistration(event_id=9, customer_name="张十四", phone="13800138012", email="zhang14@example.com", remark="德国机械工程", status="已报名"),
        ]
        db.add_all(registrations)
        
        # 插入学生服务数据（10条）
        print("正在插入测试学生服务数据...")
        services = [
            StudentAdminService(student_id=1, service_type="休学申请", start_time=datetime(2024, 9, 1, 0, 0, 0), end_time=datetime(2024, 12, 31, 0, 0, 0), reason="身体原因", status="已审批", approver_id=1, related_academic_id=1001),
            StudentAdminService(student_id=2, service_type="复学申请", start_time=datetime(2024, 3, 1, 0, 0, 0), end_time=None, reason="康复返校", status="已审批", approver_id=1, related_academic_id=1002),
            StudentAdminService(student_id=3, service_type="请假申请", start_time=datetime(2024, 11, 10, 0, 0, 0), end_time=datetime(2024, 11, 15, 0, 0, 0), reason="家中有事", status="已审批", approver_id=2, related_academic_id=1003),
            StudentAdminService(student_id=4, service_type="转专业申请", start_time=datetime(2024, 6, 1, 0, 0, 0), end_time=None, reason="兴趣不符", status="处理中", approver_id=1, related_academic_id=1004),
            StudentAdminService(student_id=5, service_type="休学申请", start_time=datetime(2024, 2, 1, 0, 0, 0), end_time=datetime(2024, 8, 31, 0, 0, 0), reason="出国交流", status="已结束", approver_id=1, related_academic_id=1005),
            StudentAdminService(student_id=1, service_type="住宿申请", start_time=datetime(2024, 8, 20, 0, 0, 0), end_time=None, reason="申请宿舍", status="已审批", approver_id=3, related_academic_id=1006),
            StudentAdminService(student_id=2, service_type="奖学金申请", start_time=datetime(2024, 10, 1, 0, 0, 0), end_time=None, reason="成绩优异", status="处理中", approver_id=1, related_academic_id=1007),
            StudentAdminService(student_id=3, service_type="缓考申请", start_time=datetime(2024, 12, 15, 0, 0, 0), end_time=None, reason="生病", status="已审批", approver_id=2, related_academic_id=1008),
            StudentAdminService(student_id=4, service_type="退学申请", start_time=datetime(2024, 5, 1, 0, 0, 0), end_time=None, reason="个人原因", status="已审批", approver_id=1, related_academic_id=1009),
            StudentAdminService(student_id=5, service_type="延长学制", start_time=datetime(2024, 9, 1, 0, 0, 0), end_time=datetime(2025, 8, 31, 0, 0, 0), reason="实习需要", status="已审批", approver_id=1, related_academic_id=1010),
        ]
        db.add_all(services)
        
        # 插入学生心理档案数据（10条）
        psych_profiles = [
            StudentPsychProfile(student_id=1, latest_emotion_tag="积极", emotion_score=85, last_interaction_time=datetime(2024, 11, 15, 10, 0, 0), emotion_history="积极,中性,积极"),
            StudentPsychProfile(student_id=2, latest_emotion_tag="中性", emotion_score=70, last_interaction_time=datetime(2024, 11, 14, 15, 0, 0), emotion_history="中性,积极,中性"),
            StudentPsychProfile(student_id=3, latest_emotion_tag="消极", emotion_score=45, last_interaction_time=datetime(2024, 11, 13, 9, 0, 0), emotion_history="中性,消极,消极"),
            StudentPsychProfile(student_id=4, latest_emotion_tag="积极", emotion_score=90, last_interaction_time=datetime(2024, 11, 12, 14, 0, 0), emotion_history="积极,积极,积极"),
            StudentPsychProfile(student_id=5, latest_emotion_tag="中性", emotion_score=65, last_interaction_time=datetime(2024, 11, 11, 16, 0, 0), emotion_history="消极,中性,中性"),
            StudentPsychProfile(student_id=6, latest_emotion_tag="积极", emotion_score=88, last_interaction_time=datetime(2024, 11, 10, 11, 0, 0), emotion_history="积极,积极,中性"),
            StudentPsychProfile(student_id=7, latest_emotion_tag="消极", emotion_score=55, last_interaction_time=datetime(2024, 11, 9, 13, 0, 0), emotion_history="中性,消极,消极"),
            StudentPsychProfile(student_id=8, latest_emotion_tag="积极", emotion_score=82, last_interaction_time=datetime(2024, 11, 8, 10, 0, 0), emotion_history="消极,中性,积极"),
            StudentPsychProfile(student_id=9, latest_emotion_tag="中性", emotion_score=72, last_interaction_time=datetime(2024, 11, 7, 15, 0, 0), emotion_history="中性,中性,积极"),
            StudentPsychProfile(student_id=10, latest_emotion_tag="积极", emotion_score=80, last_interaction_time=datetime(2024, 11, 6, 14, 0, 0), emotion_history="积极,中性,积极"),
        ]
        db.add_all(psych_profiles)
        
        # 插入学生心理预警数据（10条）
        psych_alerts = [
            StudentPsychAlert(student_id=1, trigger_reason="连续两周情绪低落", risk_level="中风险", status="处理中", teacher_id=2),
            StudentPsychAlert(student_id=2, trigger_reason="多次缺勤", risk_level="高风险", status="已干预", teacher_id=3),
            StudentPsychAlert(student_id=3, trigger_reason="情绪波动大", risk_level="低风险", status="已关注", teacher_id=2),
            StudentPsychAlert(student_id=4, trigger_reason="失眠严重", risk_level="中风险", status="处理中", teacher_id=3),
            StudentPsychAlert(student_id=5, trigger_reason="考试焦虑", risk_level="低风险", status="已关注", teacher_id=2),
            StudentPsychAlert(student_id=6, trigger_reason="社交退缩", risk_level="中风险", status="已干预", teacher_id=3),
            StudentPsychAlert(student_id=7, trigger_reason="饮食失调", risk_level="高风险", status="处理中", teacher_id=2),
            StudentPsychAlert(student_id=8, trigger_reason="学业压力大", risk_level="低风险", status="已关注", teacher_id=3),
            StudentPsychAlert(student_id=9, trigger_reason="家庭问题", risk_level="中风险", status="已干预", teacher_id=2),
            StudentPsychAlert(student_id=10, trigger_reason="抑郁倾向", risk_level="高风险", status="处理中", teacher_id=3),
        ]
        db.add_all(psych_alerts)
        
        # 插入学生反馈工单数据（10条）
        feedbacks = [
            StudentFeedbackTicket(student_id=1, content="宿舍网络问题", detail="宿舍网络经常断网，影响学习", status="已解决", solution="已联系网络中心处理", is_notified=1),
            StudentFeedbackTicket(student_id=2, content="食堂饭菜质量", detail="饭菜种类少，价格偏高", status="处理中", solution=None, is_notified=0),
            StudentFeedbackTicket(student_id=3, content="图书馆座位", detail="期末复习期间座位紧张", status="已解决", solution="增加临时自习室", is_notified=1),
            StudentFeedbackTicket(student_id=4, content="课程安排", detail="专业课时间冲突", status="处理中", solution=None, is_notified=0),
            StudentFeedbackTicket(student_id=5, content="校园安全", detail="晚上路灯不够亮", status="已解决", solution="已增加照明设备", is_notified=1),
            StudentFeedbackTicket(student_id=6, content="体育设施", detail="健身房器材老旧", status="处理中", solution=None, is_notified=0),
            StudentFeedbackTicket(student_id=7, content="宿舍卫生", detail="保洁打扫不及时", status="已解决", solution="增加保洁频次", is_notified=1),
            StudentFeedbackTicket(student_id=8, content="教材供应", detail="部分教材缺货", status="处理中", solution=None, is_notified=0),
            StudentFeedbackTicket(student_id=9, content="打印服务", detail="打印店排队时间长", status="已解决", solution="增加打印设备", is_notified=1),
            StudentFeedbackTicket(student_id=10, content="校园卡", detail="充值不方便", status="处理中", solution=None, is_notified=0),
        ]
        db.add_all(feedbacks)
        
        # 插入留学进度数据（10条）
        progresses = [
            StudyAbroadProgress(student_id=1, service_stage="文书", current_status="初稿撰写中", detail_info="文案老师正在润色PS第二段", update_by=2),
            StudyAbroadProgress(student_id=2, service_stage="选校", current_status="方案确定", detail_info="已确定8所目标院校", update_by=3),
            StudyAbroadProgress(student_id=3, service_stage="网申", current_status="材料准备", detail_info="正在准备推荐信", update_by=2),
            StudyAbroadProgress(student_id=4, service_stage="签证", current_status="已提交", detail_info="等待签证结果", update_by=3),
            StudyAbroadProgress(student_id=5, service_stage="文书", current_status="终稿审核", detail_info="PS已完成，等待审核", update_by=2),
            StudyAbroadProgress(student_id=6, service_stage="面试", current_status="准备中", detail_info="模拟面试安排在下周三", update_by=3),
            StudyAbroadProgress(student_id=7, service_stage="文书", current_status="已完成", detail_info="所有文书已提交", update_by=2),
            StudyAbroadProgress(student_id=8, service_stage="签证", current_status="已获签", detail_info="签证已下发，准备出发", update_by=3),
            StudyAbroadProgress(student_id=9, service_stage="选校", current_status="进行中", detail_info="正在评估院校匹配度", update_by=2),
            StudyAbroadProgress(student_id=10, service_stage="网申", current_status="已提交", detail_info="5所院校已完成网申", update_by=3),
        ]
        db.add_all(progresses)
        
        # 插入学生成绩数据（10条）
        print("正在插入测试学生成绩数据...")
        scores = [
            StudentScore(student_id=1, course_name="高等数学", score=92.5, semester="2024-秋季"),
            StudentScore(student_id=1, course_name="大学英语", score=85.0, semester="2024-秋季"),
            StudentScore(student_id=2, course_name="线性代数", score=88.0, semester="2024-秋季"),
            StudentScore(student_id=2, course_name="计算机基础", score=95.0, semester="2024-秋季"),
            StudentScore(student_id=3, course_name="微观经济学", score=82.0, semester="2024-秋季"),
            StudentScore(student_id=3, course_name="管理学原理", score=89.5, semester="2024-秋季"),
            StudentScore(student_id=4, course_name="电路原理", score=78.0, semester="2024-秋季"),
            StudentScore(student_id=4, course_name="工程制图", score=86.0, semester="2024-秋季"),
            StudentScore(student_id=5, course_name="艺术概论", score=91.0, semester="2024-秋季"),
            StudentScore(student_id=5, course_name="素描基础", score=87.5, semester="2024-秋季"),
        ]
        db.add_all(scores)
        
        # 插入员工日报数据（10条）
        print("正在插入测试员工日报数据...")
        reports = [
            EmployeeDailyReport(employee_id=2, report_date=date(2024, 11, 15), content="今日完成3个客户咨询，跟进了5个意向客户，整理了本周的市场活动数据。"),
            EmployeeDailyReport(employee_id=3, report_date=date(2024, 11, 15), content="完成2份文书初稿，审核了3份学生材料，与1位家长进行了沟通。"),
            EmployeeDailyReport(employee_id=4, report_date=date(2024, 11, 15), content="策划了下周的留学分享会活动，联系了5家合作院校，更新了课程宣传资料。"),
            EmployeeDailyReport(employee_id=2, report_date=date(2024, 11, 14), content="接待了8位来访客户，完成了4份留学方案设计，跟进了3个申请进度。"),
            EmployeeDailyReport(employee_id=3, report_date=date(2024, 11, 14), content="修改了5份PS文书，准备了2个面试辅导方案，参加了部门会议。"),
            EmployeeDailyReport(employee_id=4, report_date=date(2024, 11, 14), content="发布了3条社交媒体推广信息，回复了20条客户咨询，整理了本月销售数据。"),
            EmployeeDailyReport(employee_id=2, report_date=date(2024, 11, 13), content="陪同客户参加了签证面试，完成了6份申请材料的递交，跟进了10个申请进度。"),
            EmployeeDailyReport(employee_id=3, report_date=date(2024, 11, 13), content="完成了3个学生的背景评估，制定了选校方案，与海外院校进行了邮件沟通。"),
            EmployeeDailyReport(employee_id=4, report_date=date(2024, 11, 13), content="组织了内部培训会议，更新了公司官网内容，整理了活动照片。"),
            EmployeeDailyReport(employee_id=2, report_date=date(2024, 11, 12), content="完成了5个客户签约，收取了3笔服务费，安排了下周的咨询日程。"),
        ]
        db.add_all(reports)
        
        # 插入CRM意向客户数据（10条）
        print("正在插入测试CRM意向客户数据...")
        leads = [
            CrmLead(customer_name="赵六", contact_info="电话：13800138004，邮箱：zhaoliu@example.com", background_info="本科985院校，GPA 3.5，雅思7.0，意向申请美国硕士", follow_up_history="2024-11-10 首次咨询，了解美国留学流程", status="跟进中", owner_employee_id=2),
            CrmLead(customer_name="钱七", contact_info="电话：13800138005，邮箱：qianqi@example.com", background_info="本科211院校，GPA 3.2，托福95，意向申请英国硕士", follow_up_history="2024-11-12 参加了英国留学分享会", status="跟进中", owner_employee_id=3),
            CrmLead(customer_name="孙八", contact_info="电话：13800138006，邮箱：sunba@example.com", background_info="本科双非院校，GPA 3.8，雅思6.5，意向申请澳洲本科", follow_up_history="2024-11-14 进行了在线咨询", status="已签约", owner_employee_id=2),
            CrmLead(customer_name="周九", contact_info="电话：13800138007，邮箱：zhoujiu@example.com", background_info="高中在读，GPA 3.9，托福100，意向申请美国本科", follow_up_history="2024-11-8 家长陪同来访", status="跟进中", owner_employee_id=4),
            CrmLead(customer_name="吴十", contact_info="电话：13800138008，邮箱：wushi@example.com", background_info="大专毕业，工作3年，雅思6.0，意向申请加拿大专升硕", follow_up_history="2024-11-11 提交了评估申请", status="评估中", owner_employee_id=3),
            CrmLead(customer_name="郑十一", contact_info="电话：13800138009，邮箱：zheng11@example.com", background_info="硕士毕业，GPA 3.6，GRE 320，意向申请美国博士", follow_up_history="2024-11-9 咨询了套磁流程", status="跟进中", owner_employee_id=2),
            CrmLead(customer_name="王十二", contact_info="电话：13800138010，邮箱：wang12@example.com", background_info="本科985，GPA 3.4，日语N2，意向申请日本修士", follow_up_history="2024-11-13 参加了日本留学说明会", status="已签约", owner_employee_id=3),
            CrmLead(customer_name="李十三", contact_info="电话：13800138011，邮箱：li13@example.com", background_info="本科211，GPA 3.7，德语B1，意向申请德国硕士", follow_up_history="2024-11-7 咨询了APS审核", status="跟进中", owner_employee_id=4),
            CrmLead(customer_name="张十四", contact_info="电话：13800138012，邮箱：zhang14@example.com", background_info="高中在读，GPA 4.0，SAT 1500，意向申请美国TOP30", follow_up_history="2024-11-15 进行了选校咨询", status="评估中", owner_employee_id=2),
            CrmLead(customer_name="陈十五", contact_info="电话：13800138013，邮箱：chen15@example.com", background_info="本科双非，GPA 3.3，雅思7.0，意向申请香港硕士", follow_up_history="2024-11-6 首次电话咨询", status="跟进中", owner_employee_id=3),
        ]
        db.add_all(leads)
        
        db.commit()
        print("测试数据插入完成！")
        
    except Exception as e:
        db.rollback()
        print(f"插入测试数据时发生错误: {e}")
        raise
    finally:
        db.close()


def init_database():
    """
    初始化数据库：删除表、创建表、插入测试数据
    """
    print("开始初始化数据库...")
    create_tables()
    insert_test_data()
    print("数据库初始化完成！")


if __name__ == "__main__":
    init_database()
