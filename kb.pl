curso(python_basico, iniciante).
curso(html_css_fundamentos, iniciante).
curso(controle_de_versao_git, iniciante).
curso(logica_de_programacao, iniciante).
curso(python_intermediario, basico).
curso(javascript_basico, basico).
curso(sql_pratico, basico).
curso(fundamentos_web, basico).
curso(ia_para_todos, intermediario).
curso(desenvolvimento_web_avancado, intermediario).
curso(machine_learning, intermediario).
curso(engenharia_de_software, intermediario).
curso(aprendizado_profundo, avancado).
curso(otimizacao_de_modelos, avancado).
curso(arquitetura_de_sistemas, avancado).
curso(sistemas_distribuidos, avancado).

aluno(joao, iniciante).
aluno(maria, basico).
aluno(ana, iniciante).
aluno(pedro, intermediario).
aluno(luisa, basico).
aluno(carlos, avancado).
aluno(beatriz, intermediario).
aluno(rafa, iniciante).

level_index(iniciante, 0).
level_index(basico, 1).
level_index(intermediario, 2).
level_index(avancado, 3).

nivel_sucessor(NivelAluno, NivelCurso) :-
    level_index(NivelAluno, I1),
    level_index(NivelCurso, I2),
    I2 >= I1,
    I2 =< I1 + 1.

recomenda(AlunoNome, CursoNome) :-
    aluno(AlunoNome, NivelAluno),
    curso(CursoNome, NivelCurso),
    nivel_sucessor(NivelAluno, NivelCurso).

recomenda_lista(AlunoNome, ListaCursos) :-
    findall(Curso, recomenda(AlunoNome, Curso), ListaCursos).
