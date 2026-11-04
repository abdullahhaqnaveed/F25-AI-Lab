from faq_chatbot import build_bot, reply

engine = build_bot()
print("Exact answer:", reply(engine, "How do I reset my password?"))
print("Suggestion:", reply(engine, "password recovery"))
print("Empty:", reply(engine, ""))
print("Unsupported:", reply(engine, "volcano geology"))
print("New FAQ exact:", reply(engine, "What file type must my assignment be?"))
assert "it_help.txt" in reply(engine, "How do I reset my password?")
assert reply(engine, "") == "Please enter a question."
assert "No matching FAQ" in reply(engine, "volcano geology")
assert "Possible matches" in reply(engine, "password recovery")
print("FAQ behaviour checks passed")
