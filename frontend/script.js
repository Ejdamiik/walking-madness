// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {
    e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

    // this reprezentuje ten formular, ktory odosielame
    const user_input = this.querySelector("textarea").value; // Načítame text z textarea
    const im_width = document.querySelector("img").offsetWidth;

    const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
    formular.append('user-input', user_input); // Pridáme tam naše hodnoty
    formular.append('im-width', im_width);

    const url = this.action; // Nacitame povodnu URL zadanu vo formulari
    const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
    fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
        .then((res) => res.blob()) // Dostali sme binárne dáta (blob)
        .then((image) => {
            document.querySelector("#image-output").src = URL.createObjectURL(image); // Nastavíme src našeho <img> na načítaný obrázok
        })
    /*setTimeout(function(){
        scroll("output")
    }, 3000);*/
}

document.querySelector("#input-form").addEventListener("submit", handleSubmit);
