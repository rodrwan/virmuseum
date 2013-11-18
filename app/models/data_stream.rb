class DataStream < ActiveRecord::Base
  has_many :items
  belongs_to :role
  belongs_to :item
  attr_accessible :item_id, :role_id, :url, :data_type
end
