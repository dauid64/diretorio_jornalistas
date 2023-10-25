function aprovarJornalista(url) {
    token = $("#form_aprovar input[name='csrfmiddlewaretoken']").val()

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result) {
            if (result.status == 200) {
                divJornalista = document.getElementById('jornalista_' + result.id)
                divJornalista.className = ''
                divJornalista.style.display = 'none'
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: result.message,
                    showConfirmButton: false,
                    timer: 1500
                })
            } else {
                console.log('error')
                Swal.fire({
                    position: 'top-end',
                    icon: 'error',
                    title: result.message,
                    showConfirmButton: false,
                    timer: 1500
                })
            }
        }
    })
}

function reprovarJornalista(url) {
    token = $("#form_reprovar input[name='csrfmiddlewaretoken']").val()

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result) {
            if (result.status == 200) {
                divJornalista = document.getElementById('jornalista_' + result.id)
                divJornalista.className = ''
                divJornalista.style.display = 'none'
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: result.message,
                    showConfirmButton: false,
                    timer: 1500
                })
            } else {
                console.log('error')
                Swal.fire({
                    position: 'top-end',
                    icon: 'error',
                    title: result.message,
                    showConfirmButton: false,
                    timer: 1500
                })
            }
        }
    })
}