class Item < ActiveRecord::Base
  belongs_to :place
  has_many :data_streams
  belongs_to :hierarchy
  attr_accessible :name, :cientific_name, :description, :place_id, :hierarchy_id, :visits, :visible
end
