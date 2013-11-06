class AddForeignToDataStream < ActiveRecord::Migration
  def change
  	add_column :data_streams, :role_id, :integer
  	add_column :data_streams, :item_id, :integer
  end
end
