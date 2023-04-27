-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3310
-- Waktu pembuatan: 27 Apr 2023 pada 11.40
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cucci`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `orderID` int(11) NOT NULL,
  `custID` int(11) DEFAULT NULL,
  `custName` varchar(255) NOT NULL,
  `ordCat` varchar(255) NOT NULL,
  `ordDate` date NOT NULL,
  `progress` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `payment` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `orders`
--

INSERT INTO `orders` (`id`, `orderID`, `custID`, `custName`, `ordCat`, `ordDate`, `progress`, `status`, `payment`) VALUES
(6, 17573, 7, 'amara', 'Dry Clean', '2022-12-12', 'Delivered', 'Finished', 'Lunas'),
(7, 19147, NULL, 'Amara', 'Self Service', '2022-12-12', 'In The Queue', 'On Going', 'Lunas'),
(8, 14200, 7, 'amara', 'Dry Clean', '2022-12-12', 'Waiting For Pick Up', 'New', 'Belum Lunas'),
(9, 15950, NULL, 'Adinda', 'Self Service', '2022-12-13', 'On Process', 'On Going', 'Lunas'),
(10, 0, NULL, '', 'Self Service', '0000-00-00', 'On Process', 'On Going', 'Belum Lunas'),
(11, 0, NULL, 'Amira', 'Self Service', '0000-00-00', 'On Process', 'On Going', 'Belum Lunas'),
(12, 0, NULL, 'Andi', 'Self Service', '0000-00-00', 'On Process', 'On Going', 'Lunas');

-- --------------------------------------------------------

--
-- Struktur dari tabel `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `service` varchar(255) NOT NULL,
  `pickup_delivery` varchar(255) NOT NULL,
  `iron` varchar(255) NOT NULL,
  `price` int(255) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `services`
--

INSERT INTO `services` (`id`, `service`, `pickup_delivery`, `iron`, `price`, `image`) VALUES
(7, 'Dry Clean', 'No', 'No', 30000, '15167_m0851---FH4Uo2PYA-unsplash.jpg'),
(8, 'Self-Service', 'No', 'Yes', 8000, '13300_oli-woodman-nUL_PP69IPA-unsplash.jpg'),
(9, 'On-Demand', 'Yes', 'Yes', 12000, '17726_charlesdeluvio-n7Cq2rdd73E-unsplash.jpg'),
(13, 'Iron Only', 'Yes', 'Yes', 3000, '10654_immo-wegmann-zhBoLibJNgI-unsplash.jpg');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `email`, `username`, `password`, `role`) VALUES
(2, 'admin@gmail.com', 'admin', 'admin123', 'admin'),
(3, 'amara@gmail.com', 'amara', '1202200100', 'user'),
(10, 'amaraa@gmail.com', 'amarapn', '1202200100', 'admin'),
(11, 'amaraaprita@gmail.com', 'amara nadyatama', '1234560907', 'customer');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
