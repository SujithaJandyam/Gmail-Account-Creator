def validate_response(result):
    if "submitted" in result:
        print("✅ Form submitted successfully (until manual verification point).")
    elif "error" in result:
        print(f"❌ Error occurred during submission: {result}")
    else:
        print("⚠️ Unknown response.")
