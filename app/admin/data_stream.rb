ActiveAdmin.register DataStream do
	index do
        column :id
        column "Item", :item
        column "Role", :role
        column :url
        column "Tipo", :data_type
        default_actions
    end
end
