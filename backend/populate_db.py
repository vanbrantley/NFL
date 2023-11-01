import subprocess

populate_scripts = [
    'populate_teams.py',
    'populate_games.py',
    'populate_players.py',
    'populate_logs.py'
]

def run_script(script):
    try:
        print(f"Running {script}...")
        subprocess.run(['python', script], check=True)
        print(f"{script} executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")

def main():
    populate_scripts = [
        'populate_teams.py',
        'populate_games.py',
        'populate_players.py',
        'populate_logs.py',
    ]

    for script in populate_scripts:
        run_script(script)

    print("Database population completed ✅")

if __name__ == '__main__':
    main()