# OPEN FILES ===========================================
# open readme
readme = open("README.md","w+")

# open moon file
moon = open("temp_moonphase.md", "r")

# open anime file
anime = open("temp_animes.md","r")

# open part 1 of readme
part_1 = open("readme_1.md","r")

# open part 2 of readme
part_2 = open("readme_2.md","r")



# READING FILES ===========================================
# read part 1
_part_1 = part_1.read()

# read anime data
_anime = anime.read()

# read part 2
_part_2 = part_2.read()

# read moon data
_moon = moon.read()


# JOIN FILES ===========================================
# write part 1
readme.write(_part_1)

# write anime data
readme.write(_anime)

# write part 2
readme.write(_part_2)

# write moon data
readme.write(_moon)



# CLOSE FILES ==========================================
# close part 1
part_1.close()

# close part 2
part_2.close()

# close anime
anime.close()

# close moon
moon.close()

# close readme
readme.close()
