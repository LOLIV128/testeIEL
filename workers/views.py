from django.shortcuts import render
import sqlite3  

# Função que carrega os dados para ser exibido no dashboard
def dashboard(request):
    # Conecta ao banco de dados chamado 
    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("SELECT DISTINCT cargo FROM workers_workers")
    unique_jobs = [row[0] for row in c.fetchall()]

    c.execute("SELECT cargo, COUNT(*) FROM workers_workers GROUP BY cargo")
    job_counts = c.fetchall()

    c.execute("SELECT nome, salario FROM workers_workers ORDER BY salario DESC LIMIT 5")
    top_salaries = c.fetchall()

    c.execute("SELECT nome, salario FROM workers_workers ORDER BY salario ASC LIMIT 5")
    low_salaries = c.fetchall()

    c.execute("SELECT cargo, AVG(salario) FROM workers_workers GROUP BY cargo")
    avg_salaries = c.fetchall()

    c.execute("""
        SELECT cargo, nome, MAX(salario)
        FROM workers_workers
        GROUP BY cargo
    """)
    top_by_role = c.fetchall()

    
    conn.close()

    # Envia os dados para o template 'dashboard.html'
    return render(request, 'dashboard.html', {
        'unique_jobs': unique_jobs,
        'job_counts': job_counts,
        'top_salaries': top_salaries,
        'low_salaries': low_salaries,
        'avg_salaries': avg_salaries,
        'top_by_role': top_by_role,
    })
