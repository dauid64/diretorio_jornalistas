function querSerRevisor() {
    const form = document.getElementById('form_jornalista')

    Swal.fire({
        title: 'Você gostaria de se tornar um revisor?',
        text: "Revisores ajudam a validar informações de outros jornalistas!",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: 'Não',
        confirmButtonText: 'Sim, eu quero!'
      }).then((result) => {
        if (result.isConfirmed) {
          inputIsRevisor.value = 'on'
          e.preventDefault()
          form.submit()
        } else if (
            result.dismiss === Swal.DismissReason.cancel
        ) {
          form.submit()
        }
      })
}