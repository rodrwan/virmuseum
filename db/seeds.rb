# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

Place.create([ [name: "Sala 1"], [name: "Sala 2"], [name: "Sala 3"], [name: "Sala 4"], [name: "Sala 5"] ])

Role.create([ [name: 'exacto'], [name: 'popular'], [name: 'diverso'] ])

Item.create([ 
    [hierarchy_id: 10, place_id: 1, description: 'El león (Panthera leo) es un mamífero carnívoro de la familia de los félidos y una de las 4 especies del género Panthera. Algunos machos, excepcionalmente grandes, llegan a pesar hasta 250 kg, lo que los convierte en el segundo félido viviente más grande después del tigre. Los leones salvajes viven en África subsahariana y Asia, con una población en peligro crítico al noroeste de la India, habiendo desaparecido del norte de África, de Oriente Próximo y del oeste de Asia en tiempos históricos.', visits: 0, name: 'León', centific_name: 'Panthera Leo', visible: 1],
    [hierarchy_id: 10, place_id: 1, description: 'El tigre (Panthera tigris) es una de las seis especies de la subfamilia de los panterinos (familia Felidae) pertenecientes al género Panthera. Se encuentra solamente en el continente asiático; es un predador carnívoro y es la especie de felino más grande del mundo, pudiendo alcanzar un tamaño comparable al de los felinos fósiles de mayor tamaño.', visits: 0, name: 'Tigre', cientific_name: 'Panthera Tigris', visible: 1],
    [hierarchy_id: 8, place_id: 2, description: 'El lobo (Canis lupus) es una especie de mamífero placentario del orden de los carnívoros. El perro doméstico (Canis lupus familiaris) se considera miembro de la misma especie según distintos indicios, la secuencia del ADN y otros estudios genéticos.2 Los lobos fueron antaño abundantes y se distribuían por Norteamérica, Eurasia y el Oriente Medio. Actualmente, por una serie de razones relacionadas con el hombre, incluyendo el muy extendido hábito de la caza, los lobos habitan únicamente en una muy limitada porción del que antes fue su territorio.', visits: 1, name: 'Lobo', cientific_name: 'Canis Lupus', visible: 1];
  ])

User.create([ [name: "adulto", role_id: 1], [name: "niño", role_id: 1], [name: "guia", role_id: 2] ])

DataStream.create([
    [item_id: 1, role_id: 2, url: 'https://www.youtube.com/watch?v=ANbukSJdu3k', data_type: 'Video'],
    [item_id: 2, role_id: 2, url: 'https://www.youtube.com/watch?v=lolT5nIQIY4', data_type: 'Video'],
    [item_id: 3, role_id: 1, url: 'https://www.youtube.com/watch?v=PnAUMomuY9o', data_type: 'Video'];
  ])
