import alchemy.grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell = alchemy.grimoire.light_spell_record(
        "TheyShallBeLight",
        "air, fire and water"
    )
    print(f"Testing record light spell: Spell recorded: {spell}")
