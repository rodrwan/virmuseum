class Hierarchy < ActiveRecord::Base
  has_one :item
  attr_accessible :name, :description, :parent_id
end
