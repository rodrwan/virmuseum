class Item < ActiveRecord::Base
  belongs_to :place, :foreign_key => "id_place"
  attr_accessible :description, :id_data_stream, :id_place, :visits, :hierarchy
end