require 'test_helper'

class DataStreamsControllerTest < ActionController::TestCase
  setup do
    @data_stream = data_streams(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:data_streams)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create data_stream" do
    assert_difference('DataStream.count') do
      post :create, data_stream: { id_item: @data_stream.id_item, id_role: @data_stream.id_role, info: @data_stream.info, type_data: @data_stream.type_data }
    end

    assert_redirected_to data_stream_path(assigns(:data_stream))
  end

  test "should show data_stream" do
    get :show, id: @data_stream
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @data_stream
    assert_response :success
  end

  test "should update data_stream" do
    put :update, id: @data_stream, data_stream: { id_item: @data_stream.id_item, id_role: @data_stream.id_role, info: @data_stream.info, type_data: @data_stream.type_data }
    assert_redirected_to data_stream_path(assigns(:data_stream))
  end

  test "should destroy data_stream" do
    assert_difference('DataStream.count', -1) do
      delete :destroy, id: @data_stream
    end

    assert_redirected_to data_streams_path
  end
end
