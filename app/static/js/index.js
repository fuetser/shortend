const linkInput = document.querySelector("#linkInput")
linkInput.focus()

document.querySelector("#ShortenButton").addEventListener("click", e => {
    // window.location.href = linkInput.value
    if((link = linkInput.value.trim()) !== "")
    $.ajax({
      url: `/add/${link}`,
      type: "POST",
      success: responce => {
        linkInput.value = responce.link
      },
      error: (request, status, error) => {
        console.log(error)
      }
   })
})
