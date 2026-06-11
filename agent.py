def it_agent(user_input):
    response = ""

    if "vpn" in user_input.lower():
        response = """
Issue: VPN connection problem

Possible causes:
- Incorrect credentials
- Network issues
- VPN service down

Steps:
1. Check internet connection
2. Verify credentials
3. Restart VPN client

Escalate if issue persists.
"""
    elif "outlook" in user_input.lower():
        response = """
Issue: Outlook not opening

Possible causes:
- Corrupted profile
- Add-in issues

Steps:
1. Restart PC
2. Open in safe mode
3. Disable add-ins

Escalate if not resolved.
"""
    else:
        response = "Please provide more details about your IT issue."

    return response


# Test
print(it_agent("VPN not working"))
``
