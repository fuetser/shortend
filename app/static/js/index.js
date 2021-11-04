const linkInput = document.querySelector("#linkInput")
const shortLinkField = document.querySelector("#shortLink")
linkInput.focus()

const expression = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/
const regex = new RegExp(expression) 

function shortenLink() {
  var link = linkInput.value.trim()
  if(link.startsWith("http://")) link = link.replace("http://", "")
  if(link.startsWith("https://")) link = link.replace("https://", "")
  if(link.match(regex)) {
    $.ajax({
      url: "/add",
      type: "POST",
      dataType: "json",
      data: {link},
      success: responce => {
        console.log(responce)
        shortLinkField.value = `${window.location.protocol}//${window.location.host}/${responce.link}`
        },
      error: (request, status, error) => {
        console.log(error)
      }
   })
  }
}

function copy(text) {
    var input = document.createElement("textarea")
    input.innerHTML = text
    document.body.appendChild(input)
    input.select()
    var result = document.execCommand("copy")
    document.body.removeChild(input)
}

document.querySelector("#ShortenButton").addEventListener("click", e => shortenLink())
$(window).keydown(e => { if (e.keyCode === 13) shortenLink() })
document.querySelector("#copyButton").addEventListener("click", e => {
  if(shortLinkField.value !== "") copy(shortLinkField.value)
})
document.querySelector("#clearButton").addEventListener("click", e => {
  linkInput.value = ""
  shortLinkField.value = ""
})
