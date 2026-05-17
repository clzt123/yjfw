import sys
sys.path.insert(0, r'C:\Users\xx126\miniconda3\envs\0309\Lib\site-packages')

print("Testing all route imports...")

try:
    from api.student_routes import router as student_router
    print("OK: student_routes")
except Exception as e:
    print(f"FAIL: student_routes - {e}")

try:
    from api.course import router as course_router
    print("OK: course")
except Exception as e:
    print(f"FAIL: course - {e}")

try:
    from api.event import router as event_router
    print("OK: event")
except Exception as e:
    print(f"FAIL: event - {e}")

try:
    from api.student_score import router as student_score_router
    print("OK: student_score")
except Exception as e:
    print(f"FAIL: student_score - {e}")

try:
    from api.student_services import router as student_services_router
    print("OK: student_services")
except Exception as e:
    print(f"FAIL: student_services - {e}")

try:
    from api.crm_lead import router as crm_lead_router
    print("OK: crm_lead")
except Exception as e:
    print(f"FAIL: crm_lead - {e}")

try:
    from api.employee_daily_report import router as employee_daily_report_router
    print("OK: employee_daily_report")
except Exception as e:
    print(f"FAIL: employee_daily_report - {e}")

try:
    from api.student_feedback_ticket import router as student_feedback_ticket_router
    print("OK: student_feedback_ticket")
except Exception as e:
    print(f"FAIL: student_feedback_ticket - {e}")

try:
    from api.query import router as query_router
    print("OK: query")
except Exception as e:
    print(f"FAIL: query - {e}")

print("\nAll route imports tested!")