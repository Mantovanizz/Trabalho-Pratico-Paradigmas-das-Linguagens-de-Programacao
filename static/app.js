document.getElementById("form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nome = document.getElementById("aluno").value.trim().toLowerCase();

    const resp = await fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ aluno: nome })
    });

    const data = await resp.json();

    const listaUl = document.getElementById("listaCursos");
    const msg = document.getElementById("mensagem");
    const bloco = document.getElementById("resultado");

    listaUl.innerHTML = "";
    msg.textContent = "";

    if (data.erro) {
        msg.textContent = "Erro: " + data.erro;
        bloco.classList.remove("hidden");
        return;
    }

    const cursos = data.cursos;  // <--- AQUI É O QUE FALTAVA

    if (!cursos || cursos.length === 0) {
        msg.textContent = "Nenhum curso encontrado para esse aluno.";
        bloco.classList.remove("hidden");
        return;
    }

    cursos.forEach(curso => {
        const li = document.createElement("li");
        li.textContent = curso;
        listaUl.appendChild(li);
    });

    bloco.classList.remove("hidden");
});
