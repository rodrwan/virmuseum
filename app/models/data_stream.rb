class DataStream < ActiveRecord::Base
  has_many :items
  belongs_to :role, :foreign_key => "id_role"
  attr_accessible :id_item, :id_role, :info, :type_data
end
