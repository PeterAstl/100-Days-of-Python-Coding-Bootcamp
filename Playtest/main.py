

mitarbeiter = [
    {"name": "Anna", "abteilung": "IT", "gehalt": 4200},
    {"name": "Ben", "abteilung": "HR", "gehalt": 3100},
    {"name": "Clara", "abteilung": "IT", "gehalt": 4800},
    {"name": "David", "abteilung": "Marketing", "gehalt": 4100},
    {"name": "Ella", "abteilung": "IT", "gehalt": 5100},
    {"name": "Frank", "abteilung": "HR", "gehalt": 5200},
]

mitarbeiter_dict = {
    x: [
        {"name": m["name"], "gehalt_usd": round(m["gehalt"] * 1.08)}
        for m in mitarbeiter
        if m["abteilung"] == x and m["gehalt"] > 4000
    ]
    for x in sorted({m["abteilung"] for m in mitarbeiter})
    if any(m["gehalt"] > 4000 and m["abteilung"] == x for m in mitarbeiter)
}

print(mitarbeiter_dict)