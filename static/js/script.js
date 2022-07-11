
$(document).ready(function(){
    
    var baseUrl = 'http://127.0.0.1:8000/livros/listar/';
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    $(filter).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;

    });
    $(searchBtn).on('click', function(){
        searchForm.submit();
    
    });
    $(searchBtn).on('click', function(){
        searchForm.submit();

    });
});

function avaliacao(id_emprestimo){
    input_emprestimo = document.getElementById('id_emprestimo')
    input_emprestimo.value = id_emprestimo


}



