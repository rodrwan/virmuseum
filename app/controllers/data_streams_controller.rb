class DataStreamsController < ApplicationController
  # GET /data_streams
  # GET /data_streams.json
  def index
    @data_streams = DataStream.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @data_streams }
    end
  end

  # GET /data_streams/1
  # GET /data_streams/1.json
  def show
    @data_stream = DataStream.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @data_stream }
    end
  end

  # GET /data_streams/new
  # GET /data_streams/new.json
  def new
    @data_stream = DataStream.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @data_stream }
    end
  end

  # GET /data_streams/1/edit
  def edit
    @data_stream = DataStream.find(params[:id])
  end

  # POST /data_streams
  # POST /data_streams.json
  def create
    @data_stream = DataStream.new(params[:data_stream])

    respond_to do |format|
      if @data_stream.save
        format.html { redirect_to @data_stream, notice: 'Data stream was successfully created.' }
        format.json { render json: @data_stream, status: :created, location: @data_stream }
      else
        format.html { render action: "new" }
        format.json { render json: @data_stream.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /data_streams/1
  # PUT /data_streams/1.json
  def update
    @data_stream = DataStream.find(params[:id])

    respond_to do |format|
      if @data_stream.update_attributes(params[:data_stream])
        format.html { redirect_to @data_stream, notice: 'Data stream was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @data_stream.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /data_streams/1
  # DELETE /data_streams/1.json
  def destroy
    @data_stream = DataStream.find(params[:id])
    @data_stream.destroy

    respond_to do |format|
      format.html { redirect_to data_streams_url }
      format.json { head :no_content }
    end
  end
end
