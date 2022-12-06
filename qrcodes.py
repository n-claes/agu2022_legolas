import qrcode

links = {
    "accretion_2d_rho": "https://n-claes.github.io/agu2022_legolas/md_accretion.html#2d-evolution-of-density-perturbations-only",
    "accretion_2d_rho_bg": "https://n-claes.github.io/agu2022_legolas/md_accretion.html#2d-evolution-of-total-density",
    "accretion_3d_rho_v1": "https://n-claes.github.io/agu2022_legolas/md_accretion.html#3d-visualisation-of-velocity-field-with-density",
    "khi_3d": "https://n-claes.github.io/agu2022_legolas/md_khi.html#3d-evolution-of-total-velocity-and-density-field",
    "magth_3d_slices": "https://n-claes.github.io/agu2022_legolas/md_magnetothermal.html#3d-temporal-evolution-of-slices",
    "magth_3d_vfield": "https://n-claes.github.io/agu2022_legolas/md_magnetothermal.html#3d-visualisation-of-velocity-eigenfunctions",
}


def main():
    for key, link in links.items():
        img = qrcode.make(link)
        img.save(f"qrcodes/{key}.png")


if __name__ == "__main__":
    main()
