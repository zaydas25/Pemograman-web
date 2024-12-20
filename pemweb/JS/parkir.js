function hitung() {
    let jammasuk = document.getElementById("jam_masuk").value
    let jamkeluar = document.getElementById("jam_keluar").value
    let lamaparkir = jamkeluar - jammasuk
    console.log(lamaparkir)

    //biaya 2 jam pertamma
    let biayaparkir = 3000
    lamaparkir -= 2

    //hitung sisa jam
    if (lamaparkir > 0) {
        biayaparkir = biayaparkir + (lamaparkir * 1000)
    }

    console.log(biayaparkir);
    //hasilnnya
    document.getElementById("hasil").innerHTML = biayaparkir
}