class AddForeignToTermVsItems < ActiveRecord::Migration
  def change
  	add_column :term_vs_items, :term_id, :integer
  	add_column :term_vs_items, :item_id, :integer
  end
end
