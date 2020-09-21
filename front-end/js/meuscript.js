$(function() { // quando o documento estiver pronto/carregado
    
    // função para exibir mouses na tabela
    function exibir_mouses() {
        $.ajax({
            url: 'http://localhost:5000/listar_mouses',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar, // chama a função listar para processar o resultado
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar (mouses) {
            var lin = "";
            // percorrer a lista de pessoas retornadas; 
            for (mouse of mouses) { //i vale a posição no vetor
                lin += `<tr>
                    <td> ${mouse.nome}</td>
                    <td> ${mouse.marca}</td>
                    <td> ${mouse.cor}</td>
                    <td> ${mouse.peso}</td>
                    <td> ${mouse.dpi}</td>
                </tr>`;
                
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaMouses').html(lin);
            }
        }
        mostrar_conteudo("tabelaMouses");  
    }

    // função que mostra um conteúdo e esconde os outros
    function mostrar_conteudo(identificador) {
        // esconde todos os conteúdos
        $("#tabelaMouses").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        // torna o conteúdo escolhido visível
        $("#"+identificador).removeClass('invisible');      
    }

    // código para mapear o click do link Listar
    $("#linkListarMouses").click(function() {
        exibir_mouses();
    });
    
    // código para mapear click do link Inicio
    $("#linkInicio").click(function() {
        mostrar_conteudo("conteudoInicial");
    });

    // código para mapear click do botão incluir pessoa
    $('#btIncluirMouses').click(function() {
        //pegar dados da tela
        var nome = $("#campoNome").val();
        var marca = $("#campoMarca").val();
        var cor = $("#campoCor").val();
        var peso = $("#campoPeso").val();
        var dpi = $("#campoDPI").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, marca: marca, cor: cor, peso: peso, dpi: dpi });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_mouses',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: mouseIncluido, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
    });

    function mouseIncluido (retorno) {
        if (retorno.resultado == "ok") { // a operação deu certo?
            // informar resultado de sucesso
            alert("Mouse incluído com sucesso!");
            // limpar os campos
            $("#campoNome").val("");
            $("#campoMarca").val("");
            $("#campoCor").val("");
            $("#campoPeso").val("");
            $("#campoDPI").val("");
        } else {
            // informar mensagem de erro
            alert(retorno.resultado + ":" + retorno.detalhes);
        }            
    }

    function erroAoIncluir (retorno) {
        // informar mensagem de erro
        alert('Erro ao incluir!');
        // alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
    }

    // código a ser executado quando a janela de inclusão de pessoas for fechada
    $('#modalIncluirMouses').on('hide.bs.modal', function (e) {
        // se a página de listagem não estiver invisível
        if (! $("#tabelaMouses").hasClass('invisible')) {
            // atualizar a página de listagem
            exibir_mouses();
        }
    });
    // a função abaixo é executada quando a página abre
    mostrar_conteudo("conteudoInicial");
});