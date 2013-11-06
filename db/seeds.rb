# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

Place.create([ [name: "Habitacion 1"], [name: "Habitacion 2"], [name: "Habitacion 3"] ])

Role.create([ [name: "Visitante"], [name: "Guía"] ])

# Item.create([ [visits: 0, name: "Item 1", hierarchy: "mammal", description: "primer item de esta version", place_id: 1] ])

User.create([ [name: "Adulto", role_id: 1], [name: "Niño", role_id: 1], [name: "Guía", role_id: 2] ])

# DataStream.create([ [item_id: 1, role_id: 1, url: "http://www.youtube.com/watch?v=ANbukSJdu3k", data_type: "Video"] ])r