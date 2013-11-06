class TermVsItem < ActiveRecord::Base
  belongs_to :item
  belongs_to :term
  attr_accessible :count, :term_id, :item_id
end