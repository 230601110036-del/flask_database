// ======================
// VALIDASI FORM
// ======================

const bookingForm =
document.getElementById("bookingForm");

if (bookingForm) {

    bookingForm.addEventListener("submit", (e) => {

        const nama =
        document.getElementById("nama").value;

        if (nama.trim() === "") {

            alert(
                "Nama pelanggan tidak boleh kosong!"
            );

            e.preventDefault();
        }

    });

}

// ======================
// KONFIRMASI HAPUS
// ======================

const konfirmasiHapus = () => {

    return confirm(
        "Apakah Anda yakin ingin menghapus data reservasi?"
    );

};

// ======================
// NOTIFIKASI
// ======================

const notifikasi = (pesan) => {

    alert(pesan);

};