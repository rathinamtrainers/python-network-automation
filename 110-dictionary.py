student_contacts = {
    "Badara": "222-222",
    "Ajay": "123-321",
    "Sai": "9999-2222"
}
print(student_contacts)
print(f"Phone number of Ajay is {student_contacts['Ajay']}")
print(f"Phone number of Ajay is {student_contacts.get('Ajay')}")

student_contacts["DM"] = "044-123123123"
student_contacts["Ajay"] = "011-3254545"

student_contacts.pop("Badara")
print(student_contacts)

print(student_contacts.keys())
print(student_contacts.values())