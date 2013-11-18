class AddIdPlaceToItem < ActiveRecord::Migration
  def change
  	add_column :items, :place_id, :integer
    add_column :items, :hierarchy_id, :integer
  end
end
