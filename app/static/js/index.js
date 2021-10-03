const linkInput = document.querySelector("#linkInput")
const shortLinkField = document.querySelector("#shortLink")
linkInput.focus()

const expression = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/
const regex = new RegExp(expression) 


document.querySelector("#ShortenButton").addEventListener("click", e => {
    if((link = linkInput.value.trim()) !== "" && link.match(regex)) {
      $.ajax({
        url: `/add/${link.replace("/", ":")}`,
        type: "POST",
        success: responce => {
          shortLinkField.innerHTML = `${window.location.protocol}//${window.location.host}/${responce.link}`
          },
        error: (request, status, error) => {
          console.log(error)
        }
     })
    }
})
