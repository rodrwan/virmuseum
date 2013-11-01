class CreateRoles < ActiveRecord::Migration
  def change
    create_table :roles do |t|
      t.integer :id_user
      t.string :type

      t.timestamps
    end
  end
end
