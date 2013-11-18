class Term < ActiveRecord::Base
  has_many :term_vs_items
  attr_accessible :data, :count
end
