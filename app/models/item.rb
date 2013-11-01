class Item < ActiveRecord::Base
  belongs_to :place
  attr_accessible :description, :id_data_stream, :id_place, :visits, :hierarchy
end
